#include <unistd.h>

int main(){
  char* argv[] = { "./execute_me_with_rop" , "foo", "bar", NULL };
  char* envp[] = { "PABE=FUN",  NULL };
  execve("./execute_me_with_rop", argv, envp);
  return 0;
}