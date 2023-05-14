#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define BUFSIZE 1024

int scan_port(char *ip_address, int port) {
  int sockfd;
  struct sockaddr_in addr;
  char buffer[BUFSIZE];
  int num_bytes;

  /* Create a socket */
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0) {
    perror("socket");
    exit(1);
  }

  /* Set the socket options */
  setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, &timeval, sizeof(timeval));

  /* Bind the socket to the specified IP address and port */
  memset(&addr, 0, sizeof(addr));
  addr.sin_family = AF_INET;
  addr.sin_port = htons(port);
  addr.sin_addr.s_addr = inet_addr(ip_address);
  if (bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
    perror("bind");
    exit(1);
  }

  /* Connect to the specified IP address and port */
  if (connect(sockfd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
    if (errno == ECONNREFUSED) {
      return 0;
    } else {
      perror("connect");
      exit(1);
    }
  }

  /* Read from the socket */
  num_bytes = read(sockfd, buffer, BUFSIZE);
  if (num_bytes < 0) {
    perror("read");
    exit(1);
  }

  /* Close the socket */
  close(sockfd);

  /* Return the number of bytes read */
  return num_bytes;
}

int main(int argc, char *argv[]) {
  char *ip_address;
  int port_start, port_end, port;
  int num_open_ports, num_closed_ports;

  /* Check the command line arguments */
  if (argc < 3) {
    fprintf(stderr, "Usage: %s <ip_address> <port_start> <port_end>\n", argv[0]);
    exit(1);
  }

  ip_address = argv[1];
  port_start = atoi(argv[2]);
  port_end = atoi(argv[3]);

  /* Scan the specified ports */
  num_open_ports = 0;
  num_closed_ports = 0;
  for (port = port_start; port <= port_end; port++) {
    if (scan_port(ip_address, port)) {
      num_open_ports++;
    } else {
      num_closed_ports++;
    }
  }

  /* Print the results */
  printf("Open ports: %d\n", num_open_ports);
  printf("Closed ports: %d\n", num_closed_ports);

  return 0;
}
